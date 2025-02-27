from typing import Dict, Optional
import json
from datetime import datetime
import base64


class HeaderManager:
    """
    Manages HTTP headers for API requests
    """
    def __init__(self):
        self.default_headers = {
            "Content-type": "application/json",
            "Accept": "application/json"
        }

    def get_default_headers(self) -> Dict[str, str]:
        """
        Returns Default headers
        """
        return self.default_headers.copy()
    
    def add_authorization(self, headers: Dict[str,str], token: str, auth_type: str= "Bearer") -> Dict[str, str]:
        """
        Adds authorization header
        """
        headers["Authorization"]= f"{auth_type} {token}"
        return headers
    
    def add_basic_auth(self, headers: Dict[str,str], username: str, password: str= "Bearer") -> Dict[str, str]:
        """
        Adds Basic Authentication Header
        """
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64decode(credentials.encode()).decode()
        headers["Authorization"] = f"Basic{encoded_credentials}"
        return headers
    
    def add_api_key(self, headers: Dict[str,str], api_key: str, key_name: str= "X-API-Key") -> Dict[str, str]:
        """
        Adds Api Key header
        """
        headers[key_name] = api_key
        return headers
    
    def add_custom_headers(self, headers: Dict[str,str], custom_headers: Dict[str, str]) -> Dict[str, str]:
        """
        Adds Custom headers to existing headers
        """
        headers.update(custom_headers)
        return headers
    
    def add_correlation_id(self, headers: Dict[str,str], correlation_id: Optional[str]= None) -> Dict[str, str]:
        """
        Adds Correlation ID header for request tracking
        """
        if correlation_id is None:
            correlation_id = f"req-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        headers["X-Correlation-ID"] = correlation_id    
        return headers
    
    def add_content_type(self, headers: Dict[str,str], content_type: str) -> Dict[str, str]:
        """
        Sets specific content type
        """
        headers["content-Type"] = content_type  
        return headers
    
    def add_content_type(self, headers: Dict[str,str], language: str = "en-US") -> Dict[str, str]:
        """
        Adds Accept-Language header
        """
        headers["Accept-Language"] = language 
        return headers
    
    
    