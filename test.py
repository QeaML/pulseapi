import asyncio
import pulseapi

async def main():
	wp = pulseapi.Client()
	u = await wp.get_user_pulses("QML")
	print(len(u))
	await wp.close()
	
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())