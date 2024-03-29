from common.request_handler import CommandHandler

class CheckAuthCommand:
    pass

class CheckAuthCommandHandler(CommandHandler[CheckAuthCommand, None]):
    async def handle(self, command: CheckAuthCommand) -> None:
        # Replace with more auth check
        return None