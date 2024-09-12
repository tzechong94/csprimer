#define RED0 0x00
#define RED1 0x20
#define RED2 0x40
#define RED3 0x60
#define RED4 0x80
#define RED5 0xa0
#define RED6 0xc0
#define RED7 0xe0
#define GREEN0 0x00
#define GREEN1 0x04
#define GREEN2 0x08
#define GREEN3 0x0c
#define GREEN4 0x10
#define GREEN5 0x14
#define GREEN6 0x18
#define GREEN7 0x1c
#define BLUE0 0x00
#define BLUE1 0x01
#define BLUE2 0x02
#define BLUE3 0x03


// unsigned char quantize(unsigned char red, unsigned char green,
//                        unsigned char blue) {
//   unsigned char out = 0;
//   if (red < 0x20)
//     out += RED0;
//   else if (red < 0x40)
//     out += RED1;
//   else if (red < 0x60)
//     out += RED2;
//   else if (red < 0x80)
//     out += RED3;
//   else if (red < 0xa0)
//     out += RED4;
//   else if (red < 0xc0)
//     out += RED5;
//   else if (red < 0xe0)
//     out += RED6;
//   else
//     out += RED7;

//   if (green < 0x20)
//     out += GREEN0;
//   else if (green < 0x40)
//     out += GREEN1;
//   else if (green < 0x60)
//     out += GREEN2;
//   else if (green < 0x80)
//     out += GREEN3;
//   else if (green < 0xa0)
//     out += GREEN4;
//   else if (green < 0xc0)
//     out += GREEN5;
//   else if (green < 0xe0)
//     out += GREEN6;
//   else
//     out += GREEN7;

//   if (blue < 0x40)
//     out += BLUE0;
//   else if (blue < 0x80)
//     out += BLUE1;
//   else if (blue < 0xc0)
//     out += BLUE2;
//   else
//     out += BLUE3;

//   return out;
// }



// unsigned char quantize(unsigned char red, unsigned char green,
//                        unsigned char blue) {
//   unsigned char out1 = 0;
//   unsigned char out2 = 0;
//   unsigned char out3 = 0;

//   if (red < 0x20)
//     out1 += RED0;
//   else if (red < 0x40)
//     out1 += RED1;
//   else if (red < 0x60)
//     out1 += RED2;
//   else if (red < 0x80)
//     out1 += RED3;
//   else if (red < 0xa0)
//     out1 += RED4;
//   else if (red < 0xc0)
//     out1 += RED5;
//   else if (red < 0xe0)
//     out1 += RED6;
//   else
//     out1 += RED7;

//   if (green < 0x20)
//     out2 += GREEN0;
//   else if (green < 0x40)
//     out2 += GREEN1;
//   else if (green < 0x60)
//     out2 += GREEN2;
//   else if (green < 0x80)
//     out2 += GREEN3;
//   else if (green < 0xa0)
//     out2 += GREEN4;
//   else if (green < 0xc0)
//     out2 += GREEN5;
//   else if (green < 0xe0)
//     out2 += GREEN6;
//   else
//     out2 += GREEN7;

//   if (blue < 0x40)
//     out3 += BLUE0;
//   else if (blue < 0x80)
//     out3 += BLUE1;
//   else if (blue < 0xc0)
//     out3 += BLUE2;
//   else
//     out3 += BLUE3;

//   return out1+out2+out3;
// }


unsigned char quantize(unsigned char red, unsigned char green,
                       unsigned char blue) {
  
  return (red & 0xe0) | ((green & 0xe0) >> 3) | (blue >> 6);
}





// unsigned char quantize(unsigned char red, unsigned char green,
//                        unsigned char blue) {
//   const unsigned char red_quantized[] = { RED0, RED1, RED2, RED3, RED4, RED5, RED6, RED7 };
//   const unsigned char green_quantized[] = { GREEN0, GREEN1, GREEN2, GREEN3, GREEN4, GREEN5, GREEN6, GREEN7 };
//   const unsigned char blue_quantized[] = { BLUE0, BLUE1, BLUE2, BLUE3 };


//   // unsigned char out1 = red_quantized[red / 0x20];
//   // unsigned char out2 = red_quantized[green / 0x20];
//   // unsigned char out3 = red_quantized[blue / 0x40];
 
//   unsigned char out1 = red_quantized[red >> 5];
//   unsigned char out2 = green_quantized[green >> 5];
//   unsigned char out3 = blue_quantized[blue >> 6];
 
//   return out1+out2+out3;
// }


// unsigned char get_red_quantized(unsigned char red) {
//     switch (red / 0x20) {
//         case 0: return RED0;
//         case 1: return RED1;
//         case 2: return RED2;
//         case 3: return RED3;
//         case 4: return RED4;
//         case 5: return RED5;
//         case 6: return RED6;
//         case 7: return RED7;
//         default: return RED0;  // Default case
//     }
// }

// // Function to get the quantized green value using switch-case
// unsigned char get_green_quantized(unsigned char green) {
//     switch (green / 0x20) {
//         case 0: return GREEN0;
//         case 1: return GREEN1;
//         case 2: return GREEN2;
//         case 3: return GREEN3;
//         case 4: return GREEN4;
//         case 5: return GREEN5;
//         case 6: return GREEN6;
//         case 7: return GREEN7;
//         default: return GREEN0;  // Default case
//     }
// }

// // Function to get the quantized blue value using switch-case
// unsigned char get_blue_quantized(unsigned char blue) {
//     switch (blue / 0x40) {  // For blue, steps of 64 (0x40)
//         case 0: return BLUE0;
//         case 1: return BLUE1;
//         case 2: return BLUE2;
//         case 3: return BLUE3;
//         default: return BLUE0;  // Default case
//     }
// }

// // Main quantize function that sums up the quantized red, green, and blue values
// unsigned char quantize(unsigned char red, unsigned char green, unsigned char blue) {
//     unsigned char out1 = get_red_quantized(red);
//     unsigned char out2 = get_green_quantized(green);
//     unsigned char out3 = get_blue_quantized(blue);
    
//     return out1 + out2 + out3;
// }