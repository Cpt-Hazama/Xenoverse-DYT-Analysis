# Xenoverse 2 DYT Analysis Script

This is a simple script that extracts the lightwarps and color data from Xenoverse 2 DYTs. This is more-so useful for porters like myself, I'm not sure if Xenoverse 2 modders would need this at all. I made this with the idea of Garry's Mod/SFM porting in mind, as I seem to be the only person who can properly setup Xenoverse 2 materials in Source...

## Requirements
```
pip install Pillow
```

## Usage
Put the script in the directory of your DYT.DDS files, click the search bar of Explorer, type 'cmd' without quotes, then run this:
```
python dyt.py
```
It will write detailed information, in case you're a nerd like me, in the command prompt. A folder called 'DYT' will be created and inside will be every extracted lightwarp textures as well as TXT files containing your color data. Obviously, this stuff is only useful if you know how to setup your VMTs and base textures, so provided below is a correct Xenoverse 2 VMT in Source:
```
"VertexLitGeneric"
{
	"$basetexture" 				"DIR/TO/TEXTURES/white_black_basetexture"
	"$lightwarptexture" 		"DIR/TO/TEXTURES/corresponding_lightwarp_we_extracted"
	"$color2" 					"{corresponding RGB values we extracted}"

	"$bumpmap" 					"DIR/TO/TEXTURES/flat" // This is a flat normal map
	"$phongexponenttexture" 	"DIR/TO/TEXTURES/exponent" // This is a basic exponent map, R = pure white, G = dark grey, B = pure white

  "$nodecal" 					"1"

	"$phong" 					"1"
	"$phongboost"				"1"
	"$phongfresnelranges"		"[0.45 0.45 0.45]"
	"$phongalbedotint" 			"1"
}
```

Enjoy your Xenoverse 2 styled textures

## Additional Information
I'm assuming you also would like to know how to setup Xenoverse 2 base textures in Source as well for the full experience? Cool, here is my personal notes below

- In photoshop; open the base texture
- Paste alpha channel over a new pure black texture (RGB)
- Ctrl + L - Presets - DBXV2_Detail (Included in this repo)
- Ctrl + I to invert
- Save
- (Optional) if damage textures are present in the original channels, repeat the above and paste them in a new layer and layer them

You can save the DBXV2_Detail.alv to 'C:\Users\OS_USERNAME\AppData\Roaming\Adobe\Adobe Photoshop XXXX\Presets\Levels'
