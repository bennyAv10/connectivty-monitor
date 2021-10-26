# Connectivty Monitor

## Overview

Print internet connectivity status of the network \ device running it

Sample Output:
```bash
2021-10-22 12:13:35.434397 no connected  
2021-10-22 12:13:36.635399  connected  <2s

2021-10-22 12:14:01.622069  connected  <30s
2021-10-22 12:25:40.154758  connected  <15m
2021-10-22 12:36:31.180368 no connected  
2021-10-22 12:36:40.814931  connected  <10s

```

### Format

* Web [Default] run as HTTP server using port 5000 by default
  * Can set port with port parameter
* Cli - with format=cli parameter

## Usage
### Run locally
1. Clone the repository
1. Install dependencies from `requirements.txt`
    * Virtual env is recommended
1. Run: `main.py [--port PORT] {web | cli}`

I'd recommend to do this using virtual environment

### Run with Docker
1. Run `docker run -d [--env {cli | web}] [--port PORT] --name connectivity-monitor connectivity-monitor`
1. Check statud with `docker logs connectivity-monitor`

## Future plans
1. Send email alerts