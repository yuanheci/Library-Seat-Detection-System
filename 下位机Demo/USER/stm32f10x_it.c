/**
  ******************************************************************************
  * @file    GPIO/IOToggle/stm32f10x_it.c 
  * @author  MCD Application Team
  * @version V3.5.0
  * @date    08-April-2011
  * @brief   Main Interrupt Service Routines.
  *          This file provides template for all exceptions handler and peripherals
  *          interrupt service routine.
  ******************************************************************************
  * @attention
  *
  * THE PRESENT FIRMWARE WHICH IS FOR GUIDANCE ONLY AIMS AT PROVIDING CUSTOMERS
  * WITH CODING INFORMATION REGARDING THEIR PRODUCTS IN ORDER FOR THEM TO SAVE
  * TIME. AS A RESULT, STMICROELECTRONICS SHALL NOT BE HELD LIABLE FOR ANY
  * DIRECT, INDIRECT OR CONSEQUENTIAL DAMAGES WITH RESPECT TO ANY CLAIMS ARISING
  * FROM THE CONTENT OF SUCH FIRMWARE AND/OR THE USE MADE BY CUSTOMERS OF THE
  * CODING INFORMATION CONTAINED HEREIN IN CONNECTION WITH THEIR PRODUCTS.
  *
  * <h2><center>&copy; COPYRIGHT 2011 STMicroelectronics</center></h2>
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/
#include "stm32f10x_it.h" 
#include <string.h>
//#include "usart1.h"

 
void NMI_Handler(void)
{
}
 
void HardFault_Handler(void)
{
  /* Go to infinite loop when Hard Fault exception occurs */
  while (1)
  {
  }
}
 
void MemManage_Handler(void)
{
  /* Go to infinite loop when Memory Manage exception occurs */
  while (1)
  {
  }
}

 
void BusFault_Handler(void)
{
  /* Go to infinite loop when Bus Fault exception occurs */
  while (1)
  {
  }
}
 
void UsageFault_Handler(void)
{
  /* Go to infinite loop when Usage Fault exception occurs */
  while (1)
  {
  }
}
 
void SVC_Handler(void)
{
}
 
void DebugMon_Handler(void)
{
}
 
void PendSV_Handler(void)
{
}
 
void SysTick_Handler(void)
{
}

/******************************************************************************/
/*                 STM32F10x Peripherals Interrupt Handlers                   */
/*  Add here the Interrupt Handler for the used peripheral(s) (PPP), for the  */
/*  available peripheral interrupt handler's name please refer to the startup */
/*  file (startup_stm32f10x_xx.s).                                            */
/******************************************************************************/

/*********中断服务子程序************/
//u8 rec_buf[55];
//u8 idx = 0;
//u8 flag[2] = "0";
//u8 start = 0;
//u8 dis_flag = 0;

//void USART1_IRQHandler(void)                 
//{
//	 u8 r;
//	 if(USART_GetITStatus(USART1, USART_IT_RXNE) != RESET)  
//	 {
//		  r = USART_ReceiveData(USART1); //(USART1->DR);
//		  rec_buf[idx++] = r;
//		  if(r == 'a'){  //结束标志
//			  if(strcmp((char*)rec_buf, "875") == 0) flag[0] = '1';
//			  dis_flag = 1;
////			  USART_SendData(USART1, 'g');
////			  while(USART_GetFlagStatus(USART1,USART_FLAG_TC) != SET);
//		  }
//		  USART_SendData(USART1, r);
//		  while(USART_GetFlagStatus(USART1,USART_FLAG_TC) != SET);
//		  //printf("hello");
//		  //Usart_SendString(USART1, "hh");
////		  USART_SendData(USART1, 't');
////		  while(USART_GetFlagStatus(USART1,USART_FLAG_TC) != SET);
//	 } 
//	 USART_ClearFlag(USART1,USART_FLAG_TC);
//}
