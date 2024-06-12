#include "pch.h"
#define _USE_INIT_WINDOW_  // 윈도우 전역 초기화 함수를 직접 구현하도록 지정 (InitWindow)
#include <stdio.h>
#include "tipsware.h"


void InitWindow()
{
    // 창 제목을 수정한다.
    gp_window_title = "키오스크 만들기 - Step 1";
    // 윈도우 속성을 수정한다. 캡션과 테두리가 없는 기본 윈도우를 생성한다.
    g_wnd_style = WS_POPUP | WS_CLIPCHILDREN;
}
 
typedef struct AppData  // 프로그램에서 사용할 내부 데이터
{
    void *p_bk_image;  // 키오스크 배경 이미지
} AD;
 
// 컨트롤을 조작했을 때 호출할 함수 만들기
// 컨트롤의 아이디(a_ctrl_id), 컨트롤의 조작 상태(a_notify_code), 선택한 컨트롤 객체(ap_ctrl)
void OnCommand(INT32 a_ctrl_id, INT32 a_notify_code, void *ap_ctrl)
{
 
}
 
// 윈도우가 종료될 때 호출될 함수
void OnDestroy()
{
    AD *p_app = (AD *)GetAppData(); // 프로그램의 내부 데이터 주소를 얻는다.
    DeleteImageGP(p_app->p_bk_image); // 키오스크의 배경 그림을 제거한다.
}
 
// 윈도우에 발생하는 일반 메시지를 처리하는 함수
int OnUserMsg(HWND ah_wnd, UINT a_message_id, WPARAM wParam, LPARAM lParam)
{
    if (a_message_id == WM_KEYUP) {
        // ESC 키를 누르면 프로그램이 종료되도록 WM_CLOSE 메시지를 전송한다.
        if (wParam == VK_ESCAPE) PostMessage(gh_main_wnd, WM_CLOSE, 0, 0);
    }
 
    return 0;
}
 
CMD_USER_MESSAGE(OnCommand, OnDestroy, OnUserMsg)
 
int main()
{
    ChangeWorkSize(1920, 1080);   // 작업 영역 조정!
    SetWindowPos(gh_main_wnd, NULL, 0, 0, 0, 0, SWP_NOSIZE); // 윈도우를 (0,0) 위치로 이동한다.
 
    Clear(0, RGB(255, 255, 255)); // 윈도우의 배경을 RGB(255, 255, 255) 색으로 채운다!
    SetSimpleColorMode();  // 단순 색상 처리 방식으로 변경한다.
 
    AD app_data = { 0, };
    app_data.p_bk_image = LoadImageGP("kiosk\\bk.png"); // 키오스크 배경으로 사용할 그림을 읽는다.
    SetAppData(&app_data, sizeof(app_data)); // 지정한 변수를 내부 데이터로 저장  
 
    DrawImageGP(app_data.p_bk_image, 0, 0); // 배경 이미지를 화면에 출력한다.
    ShowDisplay(); // 정보를 윈도우에 출력한다.
    return 0;
}
