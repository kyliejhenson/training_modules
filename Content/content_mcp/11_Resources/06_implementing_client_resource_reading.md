# Implementing Client-Side Resource Reading

## Tags
- **Technical Skill Level**: Advanced
- **Use Case Types**: Technical implementation
- **Instructional Priority**: Applied
- **Technical Application Practice**: Yes
- **Value-Based Selling Information**: No
- **Source**: https://www.anthropic.com/learn

---

## Content

To enable resource access in your MCP client, implement a `read_resource` function. First, add the necessary imports:

```python
import json
from pydantic import AnyUrl
```

The core function makes a request to the MCP server and processes the response based on its MIME type:

```python
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)
        return resource.text
```

When you request a resource, the server returns a result with a `contents` list. The response includes the actual content (text or data), a MIME type that tells you how to parse the content, and other metadata about the resource.

The function checks the MIME type to determine how to process the content:
- If it's `application/json`, parse the text as JSON and return the parsed object
- Otherwise, return the raw text content
