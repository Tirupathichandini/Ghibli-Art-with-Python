import cv2

def ghibli_effect(image_path, save_path="ghibli_output.jpg"):
    # Load the image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 600))

    # Apply stylization filter (watercolor / Ghibli-like effect)
    ghibli = cv2.stylization(img, sigma_s=150, sigma_r=0.25)

    # Show result
    cv2.imshow("Ghibli Effect", ghibli)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite(save_path, ghibli)
    print(f"Ghibli-style image saved as {save_path}")

# Run
ghibli_effect("C:/Users/sumasree/Downloads/WhatsApp Image 2025-09-27 at 7.00.54 PM.jpeg")
