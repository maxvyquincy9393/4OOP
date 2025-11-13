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

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime
import json

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
    Prinsip SOLID : single responbility - hanya hanel Gemini API"""

    def __init__(self,prompt : str)-> str:
        """Generate respon menggunakan GEMINI api
        Dalam implementasi nyata:
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_response(prompt)
        """
        # simulasi respon
        return f"[Gemini AI response] understood yout query: {prompt}. Processing with advance AI..."

    def get_provider_name(self)-> str:
        return "Google Gemini"

    def is_available(self)-> bool:
        #cek koneksi api ( simulasi )
        return len(self.api.key) > 0

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
        timestamp = metadata.get("timestamp, 'N/A'")
        provider = metadata.get("provider", 'Unknown')

        formatted = f"""
══════════════════════════════════════╗
║  AI ASSISTANT RESPONSE              ║
╚═════════════════════════════════════╝
Provider: {provider}
Time: {timestamp}
─────────────────────────────────────
{response}
─────────────────────────────────────
"""
        return formatted

class JsonFormatter(ResponseFormatterStrategy):
    """Format response sebgai json"""

    def format(self,response: str, metadata: Dict) -> str:
        output = {
            "response": response,
            "metadata": metadata
        }
        return json.dumps(output, indent=2)

# ============================================
# 4. OBSERVER PATTERN - Event Logging
# ============================================
class Observer(ABC):
    """Observer interface untuk monitoring events"""
    @abstractmethod
    def update(self, event: str, data : Dict):
        pass

    def __init__(self,event : str, data : Dict):
        log_entry = f"[{self.name}] {event}: {data}"
        self.log.append(log_entry)
        print(f"{log_entry}")

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
    """Factory Patern : Create AI providers based on type
    Prinsip SOLID : Dependency inversion - depend om abstraction"""

    @staticmethod
    def create_provider(provider_type : str, **kwargs) -> AIProviderInterface:
        """Factory method untuk create provider
        mudah extend dengan provider baru tanpa ubah jode existing"""

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
    """Main aplication class yang mengintegrasikan semua component
    Prinsip SOLID :
    - single responbility :Manage AI abstraction
     - dependency Inversion : depend on interface, not concrate class"""

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
        """Main method untuk bertanya ke ai
        menerapkan semua pattern yang sudah dibuat"""

        self.notify_observers("request_started",{
            "question" : question,
            "provider" : self.provider.get_provider_name()
        })

    #chck porvider availableity
        if not self.provider.is_available():
            error_msg = "Ai provider not available"
            self.notify_observers("error", {"message" : error_msg})
            return error_msg

        try:
             # generate response from ai
            response = self.provider.generate_response(question)

            #simpan ke history

            converstation_entry = {
                "timestamp"    : conversation_entry["timestamp"],
                "provider" : self.provider.get_provider_name(),
                "tokens "  : len(response.split()),
                "provider" : self.provider.get_privider_name()
            }
            self.cconversation_history.append(converstation_entry)

            # format response menggunakan strategy
            metadata = {
                "timestamp" : conversation_entry["timestamp"],
                
            }