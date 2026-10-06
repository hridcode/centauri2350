# Centauri2350

Centauri2350 is a microcontroller board based off the RP2354B chip. It has 44 usable GPIO pins, plus battery charging and an audio DAC.

This is derived from my old board named "Whistle" (which honestly was trash lmao)

## Features

- 150MHz clock speed
- 520KB RAM
- 2MB flash memory
- 48 GPIOs (4 used for onboard LED + I²S connection)
- 8 analog-capable pins
- LiPo battery charging (IP5306)
- Audio DAC (PCM5102A)
- Debug pins
- USB-C connector

## Photos

### Schematic

![PCB schematic, page 1](/photos/schematic1.png)
![PCB schematic, page 2](/photos/schematic2.png)

### PCB

![PCB layout](/photos/pcb.png)

### 3D model

![3D model of PCB](/photos/3d-render.png)

## BOM

|Part|Quantity|Price|Source|
|---|---|---|---|
|RP2354B|1|$1.620|[LCSC](https://www.lcsc.com/product-detail/C39843328.html)|
|PCM5102A|1|$1.360|[LCSC](https://www.lcsc.com/product-detail/C107671.html)|
|IP5306|1|$0.280|[LCSC](https://www.lcsc.com/product-detail/C181692.html)|
|XC6206P332MR|1|$0.130|[LCSC](https://www.lcsc.com/product-detail/C5446.html)|
|X322512MSB4SI|1|$0.100|[LCSC](https://www.lcsc.com/product-detail/C9002.html)|
|USB-C receptacle|1|$0.100|[LCSC](https://www.lcsc.com/product-detail/C165948.html)|
|3.9x2.9 switch|2|$0.150|[LCSC](https://www.lcsc.com/product-detail/C202388.html)|
|PCB|1|$1.600|[JLCPCB](https://cart.jlcpcb.com/quote?stencilLayer=2&stencilWidth=100&stencilLength=100&stencilCounts=5&plateType=1&spm=Jlcpcb.Homepage.1010)|
|0402 20pF capacitor|2|$0.027|[LCSC](https://www.lcsc.com/product-detail/C1554.html)|
|0402 0.1uF capacitor|16|$0.088|[LCSC](https://www.lcsc.com/product-detail/C1525.html)|
|0402 2.2uF capacitor|4|$0.026|[LCSC](https://www.lcsc.com/product-detail/C12530.html)|
|0402 4.7uF capacitor|3|$0.063|[LCSC](https://www.lcsc.com/product-detail/C23733.html)|
|0402 10uF capacitor|10|$0.284|[LCSC](https://www.lcsc.com/product-detail/C15525.html)|
|0603 22uF capacitor|3|$0.094|[LCSC](https://www.lcsc.com/product-detail/C59461.html)|
|0402 1uH inductor|1|$0.133|[LCSC](https://www.lcsc.com/product-detail/C84468.html)|
|0402 3.3uH inductor|1|$0.028|[LCSC](https://www.lcsc.com/product-detail/C84474.html)|
|0603 2Ω resistor|2|$0.008|[LCSC](https://www.lcsc.com/product-detail/C22977.html)|
|0603 27Ω resistor|2|$0.008|[LCSC](https://www.lcsc.com/product-detail/C25190.html)|
|0402 33Ω resistor|1|$0.007|[LCSC](https://www.lcsc.com/product-detail/C25105.html)|
|0402 470Ω resistor|2|$0.013|[LCSC](https://www.lcsc.com/product-detail/C25117.html)|
|0402 1KΩ resistor|2|$0.016|[LCSC](https://www.lcsc.com/product-detail/C11702.html)|
|0402 5.1KΩ resistor|2|$0.013|[LCSC](https://www.lcsc.com/product-detail/C25905.html)|
|0603 red LED|1|$0.007|[LCSC](https://www.lcsc.com/product-detail/C2286.html)|
|Total|1|$6.155||

## Notes

Pins marked with an asterisk (*) on the board are ADC pins.
Italicized pin names denote the debug pins.

Have fun making!