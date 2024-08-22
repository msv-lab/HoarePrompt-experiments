from src.experimentation.complete.hoare_triple import Triple, parse_stmt, State
from src.experimentation.complete.helper import extract_postcondition, format_prompt
from src.common.communication import chat_with_llm, Model

VERIFYER_SYSTEM_PROMPT = """You are assigned the role of a program verifier, responsible for completing Hoare triples. Each Hoare triple is made up of three components: a precondition, a program fragment, and a postcondition. The precondition and the postcondition are expressed in natural language.

Precondition: describes the initial state of the program variables before the execution of the program fragment. This description should only include the values of the variables, without detailing the operational aspects of the program.

Program Fragment: This is a given part of the task and is not something you need to create or modify.

Postcondition: describes the state of the program variables after the execution of the program fragment with the initial state described in the precondition. This description should include both the values of the variables and the relationships between them. Similar to the precondition, avoid explaining how the program operates; concentrate solely on the variable values and their interrelations."""

generic_ctx = [
    Triple(
        "`str` is a string",
        parse_stmt("n = int(input())"),
        "`str` is a string, `n` is an input integer"),
    Triple(
        State.TOP,
        parse_stmt("i += 1"),
        "variable `i` is increased by 1"
    ),
    Triple(
        "`n` is either 3 or 5",
        parse_stmt("m = n + 1"),
        "`n` is either 3 or 5; `m` is either 4 or 6"),
    Triple(
        "`i` is integer",
        parse_stmt("j += len(str1)"),
        "`i` is integer and `j` is the length of str1"),
    Triple(
        "`n` is a positive integer",
        parse_stmt("memo = [-1] * (n + 1)"),
        "`n` is a positive integer, `memo` is a list of length n+1 with all initial values set to -1."),
]


def complete_triple(incomplete_triple: Triple, model: Model, temperature: float, context_triples=generic_ctx,
                    example_number=5):
    if len(context_triples) < example_number:
        context_triples = generic_ctx[:example_number - len(context_triples)] + context_triples
    msgs = [{"role": "system", "content": VERIFYER_SYSTEM_PROMPT}]
    for ctx in context_triples:
        msgs.append({"role": "system", "name": "example_user", "content": format_prompt(ctx)})
        msgs.append({"role": "assistant", "content": f"Postcondition: **{ctx.postcondition}**"})
    msgs.append({"role": "user", "content": format_prompt(incomplete_triple)})
    response = chat_with_llm(model=model.value, messages=msgs, temperature=temperature)
    post = extract_postcondition(response.choices[0].message.content)
    print("+" * 50)
    print(incomplete_triple)
    print(f"LLM post: {post}")
    return post
