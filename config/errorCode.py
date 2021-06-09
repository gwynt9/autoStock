def errors(err_code):
    err_dic = {0:('OP_ERR_NONE','정상처리'),
               100:('OP_ERR_LOGIN','사용자 정보교환 실패'),
               101:('OP_ERR_CONNECT','서버접속 실패'),
               102:('OP_ERR_VERSION','버전처리 실패')}