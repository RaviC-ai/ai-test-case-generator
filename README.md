# AI Test Case Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## 🎯 Overview

AI Test Case Generator is an intelligent tool that automatically generates comprehensive test cases from product requirements, user stories, and specifications using OpenAI's GPT models. This tool is designed for QA teams, test managers, and development teams to significantly reduce the time spent on manual test case creation while improving test coverage quality.

## ✨ Key Features

- 🤖 **AI-Powered Generation**: Uses OpenAI GPT to intelligently analyze requirements
- 📝 **Multiple Input Formats**: Supports text, user stories, and specification documents
- 🎨 **Customizable Test Cases**: Generate test cases for different testing types:
  - Functional Testing
  - Regression Testing
  - Edge Case Testing
  - User Acceptance Testing (UAT)
  - Performance Testing
- 📊 **Export Options**: Export test cases as CSV, JSON, or directly to test management systems
- 🔒 **Privacy-First**: Keep your requirements private with local processing options
- ⚡ **Batch Processing**: Generate test cases for multiple features simultaneously

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/RaviC-ai/ai-test-case-generator.git
cd ai-test-case-generator

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'
```

### Basic Usage

```python
from test_generator import TestCaseGenerator

# Initialize the generator
generator = TestCaseGenerator(api_key='your-openai-api-key')

# Generate test cases from a requirement
requirement = "User should be able to login with email and password"
test_cases = generator.generate(requirement, testing_type='functional')

# Display generated test cases
for test_case in test_cases:
    print(test_case)
```

## 📦 Project Structure

```
ai-test-case-generator/
├── src/
│   ├── test_generator.py       # Main generator class
│   ├── prompts.py              # GPT prompt templates
│   ├── formatters.py           # Output formatters
│   └── utils.py                # Helper utilities
├── tests/
│   ├── test_generator.py       # Unit tests
│   └── test_formatters.py      # Formatter tests
├── examples/
│   └── demo.py                 # Usage examples
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Configuration

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-api-key
MODEL=gpt-4
TEMPERATURE=0.7
MAX_TOKENS=2000
```

## 📖 Examples

See the `examples/` directory for detailed usage examples.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linting
flake8 src/
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⭐ Show Your Support

If this project helped you, please consider giving it a star! It helps others discover the project.

## 🐛 Bug Reports

Found a bug? Please create an issue with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior

## 📞 Contact & Support

For questions and support, please open an issue on GitHub.

---

**Made with ❤️ for QA professionals and test engineers**
