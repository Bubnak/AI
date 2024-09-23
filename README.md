Fine tuning of pretrained model for text summarization with Hugging Face Transformers

Model : google/pegasus-cnn_dailymail
Dataset(samsum) : https://huggingface.co/datasets/Samsung/samsum

Overview of the model training process:
    Load the pre-trained model
    Data Ingestion
    Data Validation
    Data Transformation
    Model Evaluation before fine tuning
    Model Training(fine tuning)
    Model Evaluation after fine tuning
    Compare the difference before and after the fine tuning
    Predict the text summarization

Instructions to run the API.
case 1: Directly run  Flask API
        Run main.py and check the request and response in Postman or other tool
case 2: Using Docker and Streamlit
        Run Dockerfile and get the url
        Copy paste the url in browser, streamlit view appear there you can input the paragraph or documents.


Sample API requests:

url = 'http://0.0.0.0:5000/summarize'

request type = 'post'

Input text as body in json format as shown below
{
  "text": "Test data is an integral part of the testing process for a tester. It provides information to the tester to facilitate finding defects and corrective actions. Test engineers load the application with data or stress it with huge amounts of invalid data to check breakpoints and other aspects of the application's performance. While executing test cases, test engineers need to input some data into the application to get the expected output.Test data is a production-like set of data used by test cases to determine whether an application is working correctly. Test data is usually collected into a document called a test data document that helps organize it so testers can easily access it when they run their tests.Testing the product with test data is essential when designing a new application. This can help determine if a product needs additional development or if it's ready to move on to further testing. Developers can identify coding errors by testing preliminary data before completing productivity and efficiency tests."
}

Sample Response

{
"summary": "Test data is an integral part of the testing process for a tester. Test engineers load the application with data or stress it with huge amounts of invalid data to check breakpoints and other aspects of the application's performance."
}

