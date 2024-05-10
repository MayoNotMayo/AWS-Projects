# Making a Spotify Playlist using Terraform
The following tutorial is my own recreation of the HashiCorp tutorial, so feel free to use the HashiCorp tutorial if anything requires clarity. 
(https://developer.hashicorp.com/terraform/tutorials/community-providers/spotify-playlist)

## Setup
Ensure you have installed and set up the following:

[Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) version 1.0+ 

[Docker Desktop](https://docs.docker.com/desktop/)

[Spotify Developer Account](https://developer.spotify.com/dashboard/login)

## Making the app
Log into your Spotify Developer Account and click the `CREATE AN APP` button.

In the Name field enter `Terraform Playlist Demo` and for description give it a description that makes sense to you.

Under the Redirect URI field enter 

```shell
http://localhost:27228/spotify_callback
```
This is telling spotify to find it's authorization app on port 27228 locally.

## Next we will run the authorization server
Without the authorization app, we won't be authorized to access spotify's API.

Hop into a terminal and set the environment variable to the redirect URI. This will tell the authorization server to serve what you give Spotify (the tokens) on port 27228.

In a Powershell terminal you can use 
```shell
set SPOTIFY_CLIENT_REDIRECT_URI=http://localhost:27228/spotify_callback
```

Now, in the same directory, create a file and name it `.env`

Fill the file with
```shell
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```
Head back over to the Spotify Developer site and go to the Settings of the app you created. Find the Client ID and the Client Secret and copy both of them and paste them after the `=` in the `.env` file you made.

## Running the server
Open up Docker Desktop so we can see the container when we tell the server to run.

Now open your Command line and paste in the command
```shell
docker run --rm -it -p 27228:27228 --env-file ./.env ghcr.io/conradludgate/spotify-auth-proxy
```
```diff
- Note: If docker returns an error saying it can't find ./ .env then that means the .env file you made is not in a visable place.
```

## Clone the example repository from git
Open up a new terminal window and copy and paste in
```shell
git clone https://github.com/hashicorp/learn-terraform-spotify.git
```
And then cd into the directory it made:
```
cd learn-terraform-spotify
```
## Time to get creative
Check out the `main.tf` file it made! If you read carefully you can see that it is going to make a playlist of Dolly Parton songs. I decided to change the code up a bit and so this is my final main.tf code:
```terraform
# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

terraform {
  required_providers {
    spotify = {
      version = "~> 0.2.6"
      source  = "conradludgate/spotify"
    }
  }
}

provider "spotify" {
  api_key = var.spotify_api_key
}

data "spotify_search_track" "by_artist" {
  artist = "ヨルシカ"
  album = "幻燈"
  #  name = ""
}

resource "spotify_playlist" "playlist" {
  name        = "Terraform Summer Playlist"
  description = "This playlist was created by Terraform"
  public      = true

  tracks = [
    data.spotify_search_track.by_artist.tracks[0].id,
    data.spotify_search_track.by_artist.tracks[1].id
  ]
}
```
My code is searching for songs by Yorushika, and it is searching for the first 2 songs in the Album "Magic Lantern". 

The `outputs.tf` file is going to give us our playlist url after we run terraform apply, so we can check out our playlist!

# Be sure to rename the file `terraform.tfvars.example` to `terraform.tfvars`
After you open `terraform.tfvars` replace the `...` with the API key for from the server that should still be running in the other terminal. Open the terminal and copy the API key given.

## Create the playlist
Hop back over to the other terminal.

Run the `terraform init` command to initialize terraform. Optionally run `terraform fmt` to format the `main.tf` file to look pretty.

Now run `terraform plan` to see if the code will work.

Finally, run the `terraform apply` command to create your playlist. If all goes well it will return a URL to check out the playlist created!

![image_2024-05-08_173733017](https://github.com/MayoNotMayo/AWS-Projects/assets/100898272/8b4c16dc-3875-4420-ab89-61802b1aed8b)
