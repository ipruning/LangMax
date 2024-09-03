client<llm> FastGPT {
  provider openai
  options {
    model "gpt-4o-mini"
    api_key env.OPENAI_API_KEY
  }
}

client<llm> SmartGPT {
  provider openai
  options {
    model "gpt-4o"
    api_key env.OPENAI_API_KEY
  }
}

client<llm> FastClaude {
  provider anthropic
  options {
    model "claude-3-haiku-20240307"
    api_key env.ANTHROPIC_API_KEY
  }
}

client<llm> SmartClaude {
  provider anthropic
  options {
    model "claude-3-5-sonnet-20240620"
    api_key env.ANTHROPIC_API_KEY
  }
}

client<llm> Fast {
  provider round-robin
  options {
    strategy [FastOpenAI, FastClaude]
  }
}

client<llm> Production {
  provider fallback
  options {
    strategy [SmartGPT, SmartClaude]
  }
}
