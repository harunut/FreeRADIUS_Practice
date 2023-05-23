< History >
 2023.05.23 , 로그 수집/분석기 1차 protoType 프로그램 개발 완료

 
 - 테스트용으로 두 가지 모드로 동작확인 완료(toJson, toPrint)
 - RAD_HOME으로 Radius 기본 루트 폴더 raddb 경로 설정 필요함





  > 이후 필요 작업 
    로그 처리 부분과 처리 출력 구현부 분리
    확장성을 위한 추상화 클래스를 이용하여 추후 요구사항에 맞는 기능 추가

    예외처리 클래스 메소드 세분화 ( class ExceptionTryControl(Exception): 부분 )
