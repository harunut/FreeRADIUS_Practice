
# 설정 파일을 불러와 시스템에서 사용할 수 있도록 변수를 자동으로 할당하능 제공
# 해당 파일을 import하여 설정 파일의 값 사용 용이

import os
import re

CONF_PATH = "/etc/raddb/logWatcher/logWatcher/logWatcher.conf"

def load_config(file_path=CONF_PATH):
    config = {}
    pattern = r"\$\{([^}]*)\}"  # ${} 패턴을 찾는 정규식 패턴
    
    with open(file_path, 'r') as file:
        # 파일의 각 줄을 반복하면서 파싱
        for line in file:
            line = line.strip()
            # '='를 기준으로 설정 항목과 값 분리
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # 값이 환경변수로 정의된 경우
                if re.search(pattern, value):
                    matches = re.findall(pattern, value)  # 패턴과 일치하는 모든 환경변수 추출
                    
                    # 환경변수 값이 존재하는 경우, 설정에 추가
                    for env_var_name in matches:
                        env_var_value = os.getenv(env_var_name)
                        if env_var_value:
                            value = value.replace("${" + env_var_name + "}", env_var_value)
                
                config[key] = value
    
    return config

config = load_config()

# 설정 값들을 변수로 선언
for key, value in config.items():
    exec(f"{key} = '{value}'")  # 문자열로 변수 선언