provider "aws" {
  region = "eu-west-1"
}
resource "aws_instance" "example" {
  ami           = "ami-02f3416038bdb17fb"
  instance_type = "t3.micro"
  key_name      = "<YOUR KEY PAIR NAME>"
  
  tags = {
    Name = "terraform-example"
  }
}