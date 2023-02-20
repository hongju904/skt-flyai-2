using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using GreatWall.Dialogs.Helpers;
using Microsoft.Bot.Builder.Dialogs;
using Microsoft.Bot.Connector;

//using GreatWall.Helpers;


namespace GreatWall.Dialogs
{
    [Serializable]
    public class OrderDialog:IDialog<string>
    {

        private string ServerURL = "https://labuser1storage11.blob.core.windows.net/botcontents/";
        public async Task StartAsync(IDialogContext context)
        {
            await this.MessageReceivedAsync(context, null);
        }

        private async Task MessageReceivedAsync(IDialogContext context, IAwaitable<object> result)
        {
            if (result != null) { 
                var activity = await result as Activity;

                if (activity.Text == "0") { 
                    await context.PostAsync("주문이 완료되었습니다. 감사합니다.");
                    context.Done("주문완료");
                    return;
                }
                else
                {
                    await context.PostAsync(activity.Text + "을(를) 추가 했습니다.");
                }
            }

            var message = context.MakeMessage();

            message.Attachments.Add(CardHelper.GetHeroCard("주문 완료", "지금 주문합니다", this.ServerURL + "order.png", "바로 주문", "0"));
            message.Attachments.Add(CardHelper.GetHeroCard("짜장면", "20년 전통 시그니처 메뉴!", this.ServerURL + "0001.jpg", "짜장면", "0001"));
            message.Attachments.Add(CardHelper.GetHeroCard("짬뽕", "맛있게 매운 시그니처 메뉴!", this.ServerURL + "0002.jpg", "짬뽕", "0002"));
            message.Attachments.Add(CardHelper.GetHeroCard("탕수육", "부먹/찍먹 말해주세요!", this.ServerURL + "003.jpg", "탕수육", "0003"));


            message.AttachmentLayout = "carousel";
            await context.PostAsync(message);
            context.Wait(MessageReceivedAsync);
        }
    }
}