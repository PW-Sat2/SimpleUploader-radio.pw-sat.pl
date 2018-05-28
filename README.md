## PWSat2 Radio Python module

Module requires 'credentials.json' which is generated during software download from http://pwsat2.softwaremill.com.

Credentials file format:
`{"identifier": "USER_ID", "password": "API_KEY"}`


# Usage
 `python pwsat-gs-upload.py test_frames.frames`
 
 where `test_frames.frames` file has following format:
 
 * ordinary CSV 
 * file may contain multiple frames, one frame per line
 * data format:
 
  - date and time (in pythoic way: `datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")`)
  - signle letter indicating transmission type - `U` for uplink, `D` for downlink,
  - base64-encoded almost full AX.25 frame - from AX.25 address to FCS, inclusive
  
  example:
  ```2017-11-25_00:55:48:650124,D,oK6mgqhk4KCupoKoZGED8M0DAAAAB2YAwjfYjgkNAAAAAAHLcDgAAAAAAAAAAAAAEwAAABL0TQFAXTIAxgAOAAAAAAAAAAAAAAAAAAAAAEDA/D/2PwJAd+9VMuRjdbEcugGgAHBLllcvN1VN5mLEy7xPFyJzhwgw6WJXKAYQADDbwOSufnPYuEXBiAMQPQHg59MRABCeVaAKAA8AEWEDAAwz7OLEFP/jJwAEAOYzAIDDDccIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKas=```

