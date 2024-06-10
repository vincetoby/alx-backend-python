import asyncio

async def main():
    wait_time = await wait_random(5)
    print(f"Waited for {wait_time:.2f} seconds")

# Run the main function
asyncio.run(main())

