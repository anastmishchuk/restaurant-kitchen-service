import nest_asyncio
from django.http.response import StreamingHttpResponse


class AsyncStreamingHttpResponse(StreamingHttpResponse):
    def __init__(self, streaming_content=(), *args, **kwargs):
        sync_streaming_content = self.get_sync_iterator(streaming_content)
        super().__init__(streaming_content=sync_streaming_content, *args, **kwargs)

    async def get_sync_iterator(self, async_iterator):
        nest_asyncio.apply()
        return (item for item in await async_iterator)
