# Video Membership Project

User

## Content via Vimeo

Video 
    - vimeo_id

BlogPost
    - title
    - description


Content
    - content: video / blog post / newsletter / podcast
    - data: 
        video: { vimeo_video_id: 45638849}
        blog post: { title, description, image}
    - Pricing (FK or ManyToMany)
    


## Subscription via Strip

Pricing
    - price per month
    - currency
    - id
    - name (basic/pro/business)

Subscription
    - User (FK)
    - strip_subscription_id
    - status (active / canceled / past_due / trialing)
    - Pricing (FK)
