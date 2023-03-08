import uvicorn
import fastapi

from fastapi.responses import JSONResponse

from dns_checker.core.utils import (
    csv_to_servers,
    check_servers,
    catch_exceptions,
)


class HttpAdapter:
    HOST = "0.0.0.0"
    PORT = 8080

    def __init__(self):
        fastapi_app = fastapi.FastAPI()

        @fastapi_app.exception_handler(500)
        def except_500(_, exc):
            print(exc)
            return JSONResponse(content={"message": "Internal Server Error"}, status_code=500)
        
        @catch_exceptions
        @fastapi_app.post("/domain/info")
        async def get_host_info_from_csv(file: fastapi.UploadFile = fastapi.File()):
            await self.__save_csv(file)

            result = []
            servers = csv_to_servers(str(file.filename))

            for info in check_servers(servers):
                result.append(info.to_dict())

            await self.__delete_csv(file)

            return JSONResponse(content=result)
        
        uvicorn.run(fastapi_app, host=self.HOST, port=self.PORT)


    async def __save_csv(self, file: fastapi.UploadFile):
        with open(str(file.filename), "wb") as f:
            data = await file.read()
            f.write(data)

    async def __delete_csv(self, file: fastapi.UploadFile):
        from os import remove
        remove(str(file.filename))

