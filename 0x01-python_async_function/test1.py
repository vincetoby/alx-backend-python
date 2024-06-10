import asyncio

async def main():
    n = 5
    max_delay = 10
    result = await wait_n(n, max_delay)
    print(f"Sorted wait times: {result}")

# Run the main function
asyncio.run(main())

