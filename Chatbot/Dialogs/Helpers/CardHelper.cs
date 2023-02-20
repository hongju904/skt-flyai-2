using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

using Microsoft.Bot.Connector;
using Microsoft.Bot.Builder;
using System.Collections.Specialized;
using System.Drawing;

namespace GreatWall.Dialogs.Helpers
{
    internal class CardHelper
    {

        public static Attachment GetHeroCard(string title, string subtitle, string image_url, string buttonText, string value)
        {
            List<CardImage> images = new List<CardImage>();
            images.Add(new CardImage() { Url = image_url });

            List<CardAction> actions = new List<CardAction>();
            actions.Add(new CardAction() { Title = buttonText,
                Value = value,
                Type = ActionTypes.ImBack
            });

            HeroCard card = new HeroCard()
            {
                Title = title,
                Subtitle = subtitle,
                Images = images,
                Buttons = actions
            };

            return card.ToAttachment();
        }

        CardHelper card = new CardHelper();
        // 메모리 상에 card라는 공간을 만들어 객체를 사용
        // = 인스턴스화
    }
}