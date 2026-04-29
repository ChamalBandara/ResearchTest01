# AWS Amplify Deployment Fix

The 404 error means Amplify didn't find your app to serve. For containerized Flask apps, you need to configure it properly in the AWS Console.

## Solution: Enable Container Support

1. Go to **AWS Console → Amplify**

2. Find your app `ResearchTest01`

3. Click **App settings → Build settings**

4. Click **Edit** and scroll to **Build image settings**

5. Under **Live package updates**, click **Add package**

6. Select **Docker** and choose version

7. **Important**: For container apps, you need to use AWS Elastic Beanstalk instead, OR:

## Alternative: Use Amplify with Static Hosting

Since Amplify's container support is limited, here's the easiest fix:

### Option A: Use Amplify Hosting (Static)

1. Delete the `Dockerfile` 
2. Keep only `app.py` and `amplify.yml`
3. Amplify will deploy as a static site (won't work for Flask)

### Option B: Use AWS Elastic Beanstalk (Recommended for Flask)

```bash
# Install EB CLI
pip install awsebcli

# Initialize
cd "/home/clower/Documents/Research/Application /ResearchTest01"
eb init -p docker vuln-detector

# Create environment
eb create production
```

### Option C: Use AWS Lightsail (Easiest)

1. Go to AWS Lightsail → Create instance
2. Choose "Docker" blueprint
3. Upload your Dockerfile
4. Get a public IP instantly

## Quick Fix for Amplify (If you want to try again)

Update `amplify.yml` to properly build:

```yaml
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
            - pip install flask
        build:
          commands:
            - echo "No build needed"
      artifacts:
        baseDirectory: .
        files:
          - '**/*'
    appRoot: .
```

Then in Amplify Console:
1. Go to **App settings → Rewrites and redirects**
2. Add redirect: Source address `/*` → Target address `/index.html` → Type `200`

But **Flask won't work with Amplify static hosting**. Use Elastic Beanstalk or Lightsail instead.