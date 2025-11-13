"""
===========================================
AI ASSISTANT MANAGER - OOP LEVEL LANJUTAN
===========================================

project ini mendemonstrasikan :
1. interface ( Abstract Base Class)
2. SOLID principles
3. Design Pattern ( Factory, Strategy, Observer )
4. integrasi dengan gemini AI API
5. Error handling & logging
"""
from dotenv import load_dotenv
import os
import google.generativeai as genai
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime
import json
import warnings
warnings.filterwarnings("ignore", category=UserWarning)



# ============================================
# 1. INTERFACE - Kontrak untuk semua AI Provider
# ============================================

class AIProviderInterface(ABC):
    """
    Interface untuk AI provider
    semua provider ( Gemini , Chatgpt , dll ) harus implement ini
    ini merupakaj prinsip SOLID : Interface Segregation Principle
    """

    @abstractmethod
    def generate_response(self, prompt: str)-> str:
        """Generatingg response dari AI"""
        pass

    @abstractmethod
    def get_provider_name(self):
        """DAPATKAN NAMA PROVIDER"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """cek apakah provider available"""
        pass


# ============================================
# 2. CONCRETE IMPLEMENTATION - Gemini Provider
# ===========================================

class GeminiProvider(AIProviderInterface):
    """Implenetasi konkret dari AIPROVIDERINTERFACE untuk Gemini.
    Prinsip SOLID : single responbility - hanya hanel Gemini API
    mendukung apu key dari .env"""

    def __init__(self,api_key: str = None):
        # jika api key tidak ada -> minta  lewat input
        if api_key is None or api_key.strip() == '':
            api_key = os.getenv("GEMINI_API_KEY")

            if api_key is None or api_key.strip() == '':
                api_key = input("Gemini API KEY")

        self.api_key = api_key.strip()
        self.model_name = "gemini-2.5-flash"

        self._initialize_client()

    def _initialize_client(self):
        print(f"[GEMINI] Client Initialized ({self.api_key[:6]}****)")
        try:
            genai.configure(api_key=self.api_key)
            print(f"[GEMINI] cliient initialized")
        except Exception as e:
            print(f"Gagal inisialisasi")

    def generate_response(self, prompt: str) -> str:
        """
        menggunakan api dari gemini .
        """
        try:
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:
            return f"[GEMINI error] {str(e)}"

    def get_provider_name(self) -> str:
        return "Gemini"

    def is_available(self) -> bool:
        return len(self.api_key) > 0

# ============================================
# Mock Provider untuk Testing
# ============================================
class MockAIProvider(AIProviderInterface):
    """Provider palsu untuk testing tanpa api"""

    def generate_response(self, prompt: str) -> str:
        return f"[Mock AI] Echo: {prompt}"

    def get_provider_name(self)-> str:
        return "Mock AI(Testing)"

    def is_available(self)-> bool:
        return True

# ============================================
# 3. STRATEGY PATTERN - Response Formatter
# ============================================
class ResponseFormatterStrategy(ABC):
    """Strategi pattern : berbagai cara format response
    prinsip SOLID : Open/Closed Principle - open for extension"""

    @abstractmethod
    def format(self,response: str, metadata: Dict) -> str:
        pass

class PlainTextFormatter(ABC):
    """Format response sebgai plain tect"""

    def format(self,response: str, metadata: Dict) -> str:
        return response

class DetailedFormatter(ResponseFormatterStrategy):
    """Format response dengan detail metadata"""

    def format(self,response: str, metadata: Dict) -> str:
        return f"""
╔══════════════════════════════════════╗
║        AI ASSISTANT RESPONSE         ║
╚══════════════════════════════════════╝
Provider: {metadata['provider']}
Time: {metadata['timestamp']}
───────────────────────────────────────
{response}
───────────────────────────────────────
"""
class JSONFormatter(ResponseFormatterStrategy):
    """Format response dengan detail metadata"""
    def format(self, response: str , metadata : Dict) -> str:
        return json.dumps({
            "response" : response,
            "metadata" : metadata
        }, indent=2)

# ============================================
# 4. OBSERVER PATTERN - Event Logging
# ============================================
class Observer(ABC):
    """Observer interface untuk monitoring events"""
    @abstractmethod
    def update(self, event: str, data : Dict):
        pass


class LoggerObserver(Observer):
    def __init__(self, name="SystemLogger"):
        self.name = name

    def update(self, event: str, data : Dict):
        print(f"[LOG :{self.name}] {event} -> {data} ")

class MetricCollector(Observer):
    """Collect metrics untuk analytics"""

    def __init__(self):
        self.total_request = 0
        self.total_token = 0

    def update(self, event: str, data : Dict):
        if event == "request_completed":
            self.total_request += 1
            self.total_token += data.get("token", 0)
            print(f"Metric - Tottal Request : {self.total_request}, Total Token : {self.total_token}")

# ============================================
# 5. FACTORY PATTERN - AI Provider Factory
# ============================================
class AIProviderFactory:
    """
    Factory Patern : Create AI providers based on type
    Prinsip SOLID : Dependency inversion - depend on abstraction
    """

    @staticmethod
    def create_provider(provider_type : str, **kwargs) -> AIProviderInterface:
        """
        Factory method untuk create provider
        mudah extend dengan provider baru tanpa ubah code existing
        """

        providers = {
            'gemini' : GeminiProvider,
            'mock' : MockAIProvider,
    }
        provider_class = providers.get(provider_type.lower())
        if not provider_class:
            raise ValueError(f"Unknow provider type : {provider_type}")

        return provider_class(**kwargs)

# ============================================
# 6. MAIN APPLICATION - AI Assistant Manager
# ============================================

class AIAssistantManager:
    """
    Main aplication class yang mengintegrasikan semua component
    Prinsip SOLID :
    - single responbility :Manage AI abstraction
    - dependency Inversion : depend on interface, not concrate class
    """

    def __init__(self, provider : AIProviderInterface):
        self.provider = provider
        self.observer : List[Observer] = []
        self.formatter: ResponseFormatterStrategy = PlainTextFormatter()
        self.conversation_history : List[Dict] = []

    # Observer patern method
    def attach_observer(self,observer : Observer):
        """Tambah obsercer untuk monitoring"""
        self.observer.append(observer)

    def notify_observers(self,event: str, data : Dict):
        """Notify semua observer tentang event"""
        for observer in self.observer:
            observer.update(event, data)

    # strategy pattern methods
    def set_formatter(self, formatter : ResponseFormatterStrategy):
        """Set strategy untuk format response"""
        self.formatter = formatter

    # core functionality
    def ask(self, question : str)-> str:
        """
        Main method untuk bertanya ke ai
        menerapkan semua pattern yang sudah dibuat
        """

        self.notify_observers("request_started",{
            "question" : question,
            "provider" : self.provider.get_provider_name()
        })

        #chck porvider availableity
        if not self.provider.is_available():
            return "[error] provider is not available"

        response = self.provider.generate_response(question)

        entry = {
            "timestamp" : datetime.now().isoformat(),
            "question" : question,
            "response" : response,
            "provider" : self.provider.get_provider_name(),
        }

        self.conversation_history.append(entry)

        metadata = {
            "timestamp" : entry["timestamp"],
            "provider"  : entry["provider"],
            "tokens"    : len(response.split())
        }

        output = self.formatter.format(response, metadata)

        self.notify_observers("request_completed", metadata)

        return output

    def get_conversation_summary(self):
        """Dapatkan summary dari conversation history"""
        if not self.conversation_history:
            return "No conversation yet"

        output = "\n=== CONVERSATION HISTORY ===\n"
        for i, c in enumerate(self.conversation_history,1):
            output += f"{i}. {c['timestamp']}\n Q: {c['question']}\nA: {c['response'][:80]}...\n"

        return output

# ============================================
# 7. DEMO APPLICATION
# ============================================


def demo_gemini():
    """Demo dengan egmini api
    uncomment dan gunakan key asli untuk production
    """

    print("\n" + "=" * 60)
    print("DEMO 4 . GEMINI API")
    print("=" * 60)

    api_key = os.getenv("GEMINI_API_KEY")
    provider  = AIProviderFactory.create_provider("gemini", api_key = api_key)

    assistant = AIAssistantManager(provider)
    assistant.attach_observer(LoggerObserver())
    assistant.attach_observer(MetricCollector())
    assistant.set_formatter(DetailedFormatter())

    question = input("INPUT QUESTION : ")
    print(assistant.ask(question))

if __name__ == "__main__":
    print("\n" + "=" * 60)
    api_key = os.getenv("GEMINI_API_KEY")
    provider = AIProviderFactory.create_provider("gemini", api_key = api_key)
    assistant = AIAssistantManager(provider)

    assistant.attach_observer(LoggerObserver())
    assistant.attach_observer(MetricCollector())
    assistant.set_formatter(DetailedFormatter())

    while True:
        q = input("User : ")

        if q.lower() in ["exit", "quit", "stop"]:
            print("Goodbye")
            break
        print(assistant.ask(q))


