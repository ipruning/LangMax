enum Category {
    Refund
    CancelOrder @description("some description")
    TechnicalSupport @alias("technical-help") // or alias the name
    AccountIssue
    Question
}

function ClassifyMessage(input: string) -> Category {
  client FastClaude
  prompt #"
    {# 
      This automatically injects good instructions 
      for classification since BAML knows
      Category is an enum.
    #}
    {{ ctx.output_format }}

    {{ _.role('user') }}
    {{ input }}

    {{ _.role('assistant') }}
    Response:
  "#
}
