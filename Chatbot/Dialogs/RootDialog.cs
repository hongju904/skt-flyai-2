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
        private string WelcomeMessage = "�ȳ��ϼ��� �����强 �� �Դϴ�. 1.�ֹ� 2.FAQ �߿� �����ϼ���";
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
                                Title = "���ϴ� ����� �����ϼ���",
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
                await context.PostAsync("���� �ֹ� �޴� �Դϴ�. ���ϴ� ������ �Է��� �ּ���");
                context.Call(new OrderDialog(), DialogResumeAfter);
            }
            else if (selected == "2")
            {
                await context.PostAsync("FAQ ���� �Դϴ�. ������ �Է��� �ּ���");
                context.Call(new FAQDialog(), DialogResumeAfter);
            }
            else
            {
                await context.PostAsync("�߸� �����ϼ̽��ϴ�. �ٽ� ������ �ֽñ� �ٶ��ϴ�. (1 �Ǵ� 2)");
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
                await context.PostAsync("������ ������ϴ�." + ex.Message);
            }
        }
    }
}