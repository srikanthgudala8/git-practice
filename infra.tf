# 1. Create the Database
resource "aws_dynamodb_table" "courses" {
  name           = "CloudTrainingCourses"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "course_id"

  attribute {
    name = "course_id"
    type = "S"
  }
}

# 2. Storage for Training Videos
resource "aws_s3_bucket" "training_content" {
  bucket = "my-cloud-training-content-2026"
}

# 3. Serverless Backend (Lambda)
resource "aws_lambda_function" "backend" {
  filename      = "backend.zip"
  function_name = "TrainingBackend"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "main.handler"
  runtime       = "python3.11"
}
