from typing import Dict, List
from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()

@app.get("/example/{item_id}")
async def create_items(params:str, item_id: int, id_list: List[int] = None, str_list: List[str] = None, smt_dict: Dict[str, str] = None):
    print(item_id, params)
    return {"id_list": id_list, "str_list": str_list, "smt_dict": smt_dict}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)