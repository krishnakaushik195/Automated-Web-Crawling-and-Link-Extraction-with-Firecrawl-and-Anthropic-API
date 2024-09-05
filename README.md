# Web Crawler with Firecrawl and Anthropic API Integration

## Project Overview

This project leverages the power of **Firecrawl** and **Anthropic** APIs to create a web crawler that can extract potential links and metadata from webpages. It processes main content, avoiding irrelevant sections, and outputs the results in an organized format, including title and Open Graph (OG) URL metadata.

## Features

- **Automated Web Crawling**: Efficiently scrapes webpages for relevant content.
- **Metadata Extraction**: Collects important metadata such as titles and OG URLs.
- **Link Collection**: Extracts potential links for further analysis or usage.
- **PDF Output**: Saves the collected links into a well-formatted PDF document.
  
## Requirements

- Python 3.x
- Firecrawl API key
- Anthropic API key
- dotenv for environment variable management
- FPDF for PDF generation

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/krishnakaushik195/web_.git
    cd web_
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your API keys:
    ```
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

4. Run the web crawler:
    ```bash
    python kk.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
