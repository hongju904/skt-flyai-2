using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Microsoft.Bot.Builder.Dialogs;
using Microsoft.Bot.Connector;
using System.Net.Http;
using System.Security.Policy;
using System.Text.Json;


namespace GreatWall.Dialogs
{
    [Serializable]
    public class FAQDialog : IDialog<string>
    {

        public Task StartAsync(IDialogContext context)
        {
            context.Wait(MessageReceivedAsync);
            return Task.CompletedTask;
        }

        private async Task MessageReceivedAsync(IDialogContext context, IAwaitable<object> result)
        {
            var activity = await result as Activity;
            if (activity.Text.Trim() == "그만")
            {
                context.Done("답변완료");
            }
            else
            {
                // 실제 답변 코드
                string uri = "https://labuser20test.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=labuser20&api-version=2021-10-01&deploymentName=production";
                string subscriptionKey = "33266a0dc01c43da8f79dce436c445d6";
                string question = activity.Text;

                var requestBody = new
                {
                    top = 3,
                    question,
                    includeUnstructuredSources = true,
                    //confidenceScoreThreshold = scoreThreshold,
                    //answerSpanRequest = new { enable = true, topAnswersWithSpan = 1, confidenceScoreThreshold = scoreThreshold },
                    //filters = new { metadataFilter = new { logicalOperation, metadata = new[] { new { key = metadataKey, value = metadataValue } } } }
                };

                var client = new HttpClient();
                client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);

                var response = await client.PostAsync(uri, new StringContent(JsonSerializer.Serialize(requestBody), System.Text.Encoding.UTF8, "application/json"));

                var responseContent = await response.Content.ReadAsStringAsync();
                await context.PostAsync(responseContent);

                context.Wait(MessageReceivedAsync);
            }
        }
    }
}