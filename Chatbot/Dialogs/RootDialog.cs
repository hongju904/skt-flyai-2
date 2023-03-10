using System;
using System.Threading.Tasks;

using Microsoft.Bot.Connector;
using Microsoft.Bot.Builder.Dialogs;
using System.Net.Http;
using GreatWall.Dialogs;
using System.Collections.Generic;
//using System.EnterpriseServices;


namespace GreatWall
{
    [Serializable]
    public class RootDialog : IDialog<object>
    {
        private string WelcomeMessage = "안녕하세요 만리장성 봇 입니다. 1.주문 2.FAQ 중에 선택하세요";
        public async Task StartAsync(IDialogContext context)
        {
            context.Wait(MessageReceivedAsync);
        }


        public async Task MessageReceivedAsync(IDialogContext context, IAwaitable<object> argument)
        {
            var activity = await argument;
            await context.PostAsync(WelcomeMessage);

            var message = context.MakeMessage();
            var actions = new List<CardAction>();
            actions.Add(new CardAction() { Title = "1. Order", Value = "1", Type = ActionTypes.ImBack });
            actions.Add(new CardAction() { Title = "2. FAQ", Value = "2", Type = ActionTypes.ImBack });

            message.Attachments.Add(
                            new HeroCard
                            {
                                Title = "원하는 기능을 선택하세요",
                                Buttons = actions
                            }.ToAttachment()
                );

            await context.PostAsync(message);

            context.Wait(SendWelcomeMessageAaync);
        }

        private async Task SendWelcomeMessageAaync(IDialogContext context, IAwaitable<object> result)
        {
            var activity = await result as Activity;
            string selected = activity.Text.Trim();

            if (selected == "1")
            {
                await context.PostAsync("음식 주문 메뉴 입니다. 원하는 음식을 입력해 주세요");
                context.Call(new OrderDialog(), DialogResumeAfter);
            }
            else if (selected == "2")
            {
                await context.PostAsync("FAQ 서비스 입니다. 질문을 입력해 주세요");
                context.Call(new FAQDialog(), DialogResumeAfter);
            }
            else
            {
                await context.PostAsync("잘못 선택하셨습니다. 다시 선택해 주시기 바랍니다. (1 또는 2)");
            }
        }

        private async Task DialogResumeAfter(IDialogContext context, IAwaitable<string> result)
        {
            try
            {
                string message = await result;
                await this.MessageReceivedAsync(context, result);
            }
            catch (Exception ex)
            {
                await context.PostAsync("오류가 생겼습니다." + ex.Message);
            }
        }
    }
}