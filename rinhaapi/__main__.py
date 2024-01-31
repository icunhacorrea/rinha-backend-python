import uvicorn 

def main():
    uvicorn.run("rinhaapi.api:app", port=8000, reload=True)

if __name__=="__main__":
    main()
