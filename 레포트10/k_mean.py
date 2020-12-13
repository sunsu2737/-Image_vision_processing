import cv2
import numpy as np
import openimg


def k_mean_gray(img, k=2):
    centers = [np.random.randint(0, 255) for _ in range(k)]

    row, col = img.shape
    for i in range(10):
        print(i+1)
        association = {i: [] for i in centers}
        for x in range(row):
            for y in range(col):
                d_c = 300
                d_i = 0
                for c in centers:
                    if np.abs(c-img[x, y]) < d_c:
                        d_c = np.abs(c-img[x, y])
                        d_i = c

                association[d_i].append(img[x, y])
        centers = []
        for key, vals in association.items():
            centers.append(sum(vals)//len(vals))
    new_img = np.zeros((row, col), dtype=np.uint8)
    for key in association.keys():
        association[key] = set(association[key])
    print(association)
    for x in range(row):
        print(x)
        for y in range(col):

            d_c = 300
            d_i = 0
            for c in centers:
                if np.abs(c-img[x, y]) < d_c:
                    d_c = np.abs(c-img[x, y])
                    d_i = c
            new_img[x, y] = d_i

    return new_img


def k_mean_color(img, k=2):
    centers = [(np.random.randint(0, 255), np.random.randint(
        0, 255), np.random.randint(0, 255)) for _ in range(k)]

    row, col, chanel = img.shape

    for i in range(10):
        print(i+1)
        association = {i: [] for i in centers}
        for x in range(row):
            for y in range(col):
                d_c = 9999
                d_i = 0
                for c in centers:
                    if np.sqrt(np.power(c[0]-img[x, y, 0], 2)+np.power(c[1]-img[x, y, 1], 2)+np.power(c[2]-img[x, y, 2], 2)) < d_c:
                        d_c = np.sqrt(np.power(
                            c[0]-img[x, y, 0], 2)+np.power(c[1]-img[x, y, 1], 2)+np.power(c[2]-img[x, y, 2], 2))
                        d_i = c

                association[d_i].append(img[x, y])
        centers = []
        for key, vals in association.items():
            v0 = 0
            v1 = 0
            v2 = 0
            for v in vals:
                v0 += v[0]
                v1 += v[1]
                v2 += v[2]
            centers.append((v0/len(vals), v1/len(vals), v2/len(vals)))
    new_img = np.zeros((row, col, chanel), dtype=np.uint8)

    for x in range(row):
        print(x)
        for y in range(col):

            d_c = 9999
            d_i = 0
            for c in centers:
                if np.sqrt(np.power(c[0]-img[x, y, 0], 2)+np.power(c[1]-img[x, y, 1], 2)+np.power(c[2]-img[x, y, 2], 2)) < d_c:
                    d_c = np.sqrt(np.power(
                        c[0]-img[x, y, 0], 2)+np.power(c[1]-img[x, y, 1], 2)+np.power(c[2]-img[x, y, 2], 2))
                    d_i = c

            new_img[x, y] = d_i

    return new_img


if __name__ == '__main__':
    img = cv2.imread("Lenna.png")
    gray_img=openimg.toGray(img)
    new_img = k_mean_gray(gray_img)
    new_img2 = k_mean_color(img)
    cv2.imshow("src", img)
    cv2.imshow("gray",gray_img)
    cv2.imshow("k_mean_gray", new_img)
    cv2.imshow("k_mean_color", new_img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
