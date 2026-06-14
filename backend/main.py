import httpx

async def get_twitch_user(username: str, client_id: str, access_token: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://api.twitch.tv/helix/users",
            params={"login": username},
            headers={
                "Client-Id": client_id,
                "Authorization": f"Bearer {access_token}",
            }
        )
        data = resp.json()
        user = data["data"][0]
        return user["profile_image_url"]  # e.g. https://static-cdn.jtvnw.net/...
    
    resp = await client.post(
    "https://id.twitch.tv/oauth2/token",
    params={
        "client_id": YOUR_CLIENT_ID,
        "client_secret": YOUR_CLIENT_SECRET,
        "grant_type": "client_credentials",
    }
)
    access_token = resp.json()["access_token"]

    
