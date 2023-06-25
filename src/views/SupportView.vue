<template>
  <v-container style="margin-top: 12px; margin-bottom: 12px">
    <v-row>
      <v-col cols="12" xl="12">
        <strong>WAYS TO SUPPORT THE FACE FRIENDS FOUNDATION</strong>
        <v-img src="@/assets/Support/cover.webp" style="margin-top: 24px" />
      </v-col>
      <v-col cols="12" xs="12">
        <v-card style="display: flex; flex-direction: column; align-items: center">
          <v-card-title>SUPPORT THE FACE FRIENDS FOUNDATION</v-card-title>
          <div style="margin-left: 5vw; margin-right: 5vw">Every dime donated to The Face Friends Foundation goes toward our mission of achieving food, educational, health, and financial security services for the community. With your financial donation, needy families in Jamaica and the United States can have food on their table and in their cupboard, clothes on their backs, backpacks for their children to go to school, youth mentoring and tutoring programs, and financial assistance to overcome emergencies and hardships. Please help our mission by making an online donation today.</div>
          <div style="margin-left: 5vw; margin-right: 5vw; display: flex; flex-direction: row">
            <div style="margin-top: 16px; margin-bottom: 16px">You can also contact us to make a donation via email
              <a href="mailto:donate@facefriendsfoundation.com">donate@facefriendsfoundation.com</a>
              or phone 678-765-0482.
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="display: flex; flex-direction: column; align-items: center">
          <v-img src="@/assets/Support/shop.webp" />
          <v-card-title>SHOP</v-card-title>
          <v-card-text>There are other ways to support our mission other than donating, you can go to our Foundation shop online and purchase an item. </v-card-text>
          <div style="margin: 16px; display: flex; justify-content: center">
            <v-btn :href="link1" target="_blank">SHOP AT THE THREE FS STORE</v-btn>
          </div>
        </v-card>
      </v-col>
      <v-col cols="12" sm="12" md="6" lg="6" xl="6">
        <v-card style="height: 100%; display: flex; flex-direction: column; align-items: center">
          <v-img src="@/assets/Support/car.webp" />
          <v-card-title>CAR DONATION PROGRAM</v-card-title>
          <strong> Step 1:  Click on the link below</strong>
          <div style="margin: 10px">Click on the link below and complete the donation form online or by calling us at (888) 755-5435. We will ask you a few questions about your vehicle, including the VIN, year, make, model, mileage, and condition.</div>
          <strong>Step 2:  Schedule Free Car Pick Up</strong>
          <div style="margin: 10px">Tell us a bit about yourself and where your car will be picked up. You’ll be contacted by a local towing agent within 2-3 business days to schedule a pick up time that works best for you.</div>
          <strong>Step 3:  Get Tax Receipt</strong>
          <div style="margin: 10px">Once you submit your car donation through the FFF Vehicle Donation Program, you’ll receive a confirmation email with access to your Donor Console. Within the Donor Console, you’ll be able to track the progress of your car donation, upload documents, and get tax and title information. After your car is sold, you will be emailed a tax receipt.</div>
          <div style="margin: 16px; display: flex; justify-content: center">
            <v-btn :href="link2" target="_blank">CAR DONATION PROGRAM</v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" xs="12" sm="6">
        <v-card style="height: 100%; object-fit: cover">
          <v-img src="@/assets/Support/img.webp" style="height: 100%"></v-img>
        </v-card>
      </v-col>
      <v-col cols="12" xs="12" sm="6">
        <v-card style="height: 100%">
          <v-card-text class="text-h4 font-weight-bold" style="margin-bottom: 4px">
            HELP OUR CAUSE
          </v-card-text>
          <div style="margin-left: 20px; margin-bottom: 20px">
            <div style="display: flex; flex-direction: column; justify-content: center;">
              <div>
                <v-btn style="margin-bottom: 20px;" :href="link3" target="_blank">Donate</v-btn>
              </div>
              <v-img src="@/assets/Support/payments.png" max-width="200"></v-img>
            </div>
          </div>
          <v-card-text>
            100% of your donation will fund our mission to provide support and improve conditions for those in need. All donations are tax deductible.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'SupportView',
    // 这里是组件的JavaScript代码
    data() {
      return {
        link1: "https://www.facefriendsfoundation.org",
        link2: "https://www.cardonationwizard.com/cars-for-charity/donate/donate-a-car-for-charity.html?ref=cars-for-charity&affilID=Face%20Friends%20Foundation%2C%20Incorporated&affilName=Face%20Friends%20Foundation%2C%20Incorporated",
        link3: "https://www.paypal.com/webapps/shoppingcart?flowlogging_id=f418588899cbc&mfid=1686273977343_f418588899cbc#/checkout/openButton"
      }
    }
  }
</script>

<style scoped>
  /* 这里是关于页面的CSS样式 */
</style>  