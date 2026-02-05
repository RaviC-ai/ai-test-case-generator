"""AI Test Case Generator - Main Module

This module provides the core functionality for generating test cases
using OpenAI's GPT models based on product requirements and specifications.
"""

import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
import openai
from pydantic import BaseModel

# Load environment variables
load_dotenv()


class TestCase(BaseModel):
    """Data model for a generated test case."""
    test_id: str
    title: str
    description: str
    preconditions: List[str]
    steps: List[str]
    expected_result: str
    test_type: str


class TestCaseGenerator:
    """Generate test cases using OpenAI GPT models."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the test case generator.
        
        Args:
            api_key: OpenAI API key. If not provided, uses OPENAI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError('OpenAI API key not found')
        
        openai.api_key = self.api_key
        self.model = os.getenv('MODEL', 'gpt-3.5-turbo')
        self.temperature = float(os.getenv('TEMPERATURE', 0.7))
        self.max_tokens = int(os.getenv('MAX_TOKENS', 2000))

    def generate(
        self,
        requirement: str,
        testing_type: str = 'functional',
        num_cases: int = 5
    ) -> List[TestCase]:
        """Generate test cases from a requirement.
        
        Args:
            requirement: Product requirement or user story
            testing_type: Type of testing (functional, regression, edge_case, etc.)
            num_cases: Number of test cases to generate
            
        Returns:
            List of generated TestCase objects
        """
        prompt = self._build_prompt(requirement, testing_type, num_cases)
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': 'You are a QA expert generating comprehensive test cases.'},
                    {'role': 'user', 'content': prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            test_cases = self._parse_response(response.choices[0].message.content)
            return test_cases
            
        except Exception as e:
            print(f'Error generating test cases: {str(e)}')
            return []

    def _build_prompt(self, requirement: str, testing_type: str, num_cases: int) -> str:
        """Build the prompt for GPT."""
        return f"""Generate {num_cases} detailed {testing_type} test cases for the following requirement:
        
Requirement: {requirement}

For each test case, provide:
1. Test ID (e.g., TC001)
2. Title
3. Description
4. Preconditions
5. Steps
6. Expected Result

Format as structured JSON."""

    def _parse_response(self, response_text: str) -> List[TestCase]:
        """Parse GPT response into TestCase objects."""
        test_cases = []
        # Implementation for parsing response
        return test_cases


if __name__ == '__main__':
    # Example usage
    generator = TestCaseGenerator()
    requirement = 'User should be able to login with email and password'
    test_cases = generator.generate(requirement, testing_type='functional')
    
    for tc in test_cases:
        print(tc)
