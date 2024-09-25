package com.capstone.chatBotServer.App.Controller;

import java.net.URLEncoder;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.capstone.chatBotServer.App.Dto.CMRespDto;
import com.capstone.chatBotServer.Service.chatBotserviceImpl;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@RestController
@RequestMapping("/c1/chatBot")
public class chatBotController {

	private final chatBotserviceImpl chatBotserviceImpl;
	// 플러터에서 메세지 받기 확인
	// 스프링에서 메세지 가공 후 전송
	// 파이썬에게 API 호출
	@PostMapping("/send")
	public ResponseEntity<?> sendMessage(@RequestBody String userMessage){
		boolean status = true;
		
		try {
			System.out.println(userMessage);
			String AIMessage = chatBotserviceImpl.sendToPythonMessage(userMessage);
			// 보내기 전에 인코딩
			
			String encodeMessage = URLEncoder.encode(AIMessage);
			return ResponseEntity.ok().body(new CMRespDto<>(1,"메세지 전송 성공",encodeMessage));
		} catch (Exception e) {
			status = false;
			return ResponseEntity.ok().body(new CMRespDto<>(1,"메세지 전송 실패",status));
		}

	}
}
