provider "aws" {
  region = "us-east-1" 
}

resource "aws_vpc" "Nimesha" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.Nimesha.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a" 
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.Nimesha.id
  cidr_block = "10.0.2.0/24"
  availability_zone       = "us-east-1b" 
}

resource "aws_security_group" "Nimesha" {
  name        = "Nimesha-security-group"
  description = "Nimesha security group"
  vpc_id      = aws_vpc.Nimesha.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "Nimesha" {
  ami           = "ami-03a6eaae9938c858c"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id
  key_name      = "nimesha"
  associate_public_ip_address = true

  security_groups = [aws_security_group.Nimesha.id]

  root_block_device {
    volume_size = 8
    volume_type = "gp2"
    delete_on_termination = true
  }

  tags = {
    Name    = "Assignment EC2"
    purpose = "Assignment"
  }
}
