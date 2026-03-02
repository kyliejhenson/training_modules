# Implementing Client-Side Prompt Functions

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

To use prompts from your client, implement two functions: `list_prompts` and `get_prompt`.

**List Prompts**

```python
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

**Get Prompt with Variable Interpolation**

```python
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

When you request a prompt, you provide arguments that get passed to the prompt function as keyword arguments. For example, if your server has a `format_document` prompt that expects a `doc_id` parameter, the arguments dictionary would contain `{"doc_id": "plan.md"}`. This value gets interpolated into the prompt template.
