# create a mask
mask = np.zeros(grayImage.shape[:2], np.uint8)
mask[100: 400, 50:250] = 255
masked_img = cv2.bitwise_and(grayImage,grayImage,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([grayImage],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([grayImage],[0],mask,[256],[0,256])
plot.subplot(221), plot.imshow(grayImage, 'gray')
plot.subplot(222), plot.imshow(mask,'gray')
plot.subplot(223), plot.imshow(masked_img, 'gray')
plot.subplot(224), plot.plot(hist_full), plot.plot(hist_mask)
plot.xlim([0,256])
plot.show()
