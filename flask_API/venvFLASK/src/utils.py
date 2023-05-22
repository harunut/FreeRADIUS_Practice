from typing import Dict, Any, List
from subprocess import check_output
from shlex import split

OPERATION_RADTEST_LIST: List[str] = ["pap", "mschap", "chap"]
OPERATION_EAPOLTEST_LIST: List[str] = ["mschapv2"]

def sendAuthRequest(id: str, pw: str, auth: str) -> Dict[str, Any]:
    # Python 함수 작성에 도움이 되는 typing 모듈을 이용하여 어노테이션을 진행했음.
    # 해당 함수의 결과는 API 통신에 사용되므로 JSON 형태로 쓰임이 자명하지만, 
    # 호출하는 쪽에서 JSON 변환하는 쪽으로 해당 함수에서는 처리하지 않는다.
    
    if auth in OPERATION_RADTEST_LIST:
        cmd = f'req_auth -u {id} -p {pw} -a {auth}'
        output = check_output(split(cmd)).decode('utf-8')
    
    elif auth in OPERATION_EAPOLTEST_LIST:
        cmd = f'req_auth -e -u {id} -p {pw} -a {auth}'    
        output = check_output(split(cmd)).decode('utf-8')
    
    else:
        raise ValueError(f"Invalid auth method: {auth}")
    
    result:str = str()
    for line in output.split("\n"):
        if line.startswith("Received"):
            index = line.find(" ")
            if index != -1:
                response = line[index+1:]
                if response.find("Access-Accept") != -1:
                    result = "Access-Accept"
                    break
                else:
                    result = "Failed, Access-Reject"
                    break
                    
    return {'userName':id,
        'password':pw,
        'auth':auth,
        'result':result}
