import asyncio
from glide_sync import GlideClientConfiguration, NodeAddress, GlideClient

addresses = [NodeAddress("localhost", 6379)]
config = GlideClientConfiguration(addresses, request_timeout=500)
client = GlideClient.create(config)
