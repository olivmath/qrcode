use clap::Parser;
use image::Luma;
use qrcode::QrCode;
use std::env;

#[derive(Parser)]
#[clap(name = "myqr", about = "A QR code generator and decoder CLI tool")]
struct Cli {
    #[clap(subcommand)]
    command: Commands,
}

#[derive(Parser)]
enum Commands {
    Generate {
        #[clap(help = "Text to encode in the QR code")]
        text: String,

        #[clap(
            help = "Filename to save the QR code. If no extension is provided, .png will be appended"
        )]
        filename: String,
    },
    Decode {
        #[clap(help = "Path to the QR code image file")]
        path: String,
    },
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();

    match &cli.command {
        Commands::Generate { text, filename } => {
            let code = QrCode::new(text.as_bytes())?;
            let image = code.render::<Luma<u8>>().build();

            let mut output_path =
                dirs::download_dir().unwrap_or_else(|| env::current_dir().unwrap());
            output_path.push(filename);

            if output_path.extension().is_none() {
                output_path.set_extension("png");
            }

            image.save(&output_path)?;
            println!("QR code saved to {}", output_path.display());
        }
        Commands::Decode { path } => {
            let results = decode_qr_code(path)?;

            if results.is_empty() {
                println!("No QR codes found in the image.");
            } else {
                for (i, result) in results.into_iter().enumerate() {
                    match result {
                        Ok(text) => println!("QR code {}: {}", i + 1, text),
                        Err(e) => println!("Error decoding QR code {}: {}", i + 1, e),
                    }
                }
            }
        }
    }

    Ok(())
}

fn decode_qr_code(
    image_path: &str,
) -> Result<Vec<anyhow::Result<String>>, Box<dyn std::error::Error>> {
    let img = image::open(image_path)?;
    let decoder = bardecoder::Decoder::default();
    Ok(decoder.decode(&img))
}
