#include <iostream>
#include <cstring>
#include <string>
#include <cstdint>
#include <string_view>
#include <sstream>
#include <array>
#include <memory>
#include <openssl/md5.h>

void Md5() {
    std::uint32_t i{1};
    bool five{false}, six{false};
    while(true) {
        std::stringstream tmp;
	tmp << "yzbqklnj" << i;
        std::string_view input{tmp.str()};

        unsigned char digest[16];
	MD5(reinterpret_cast<const unsigned char*>(input.data()), input.size(), digest);

        char j[6];
        for(auto k = 0; k<3; k++) {
            std::sprintf(j + k*2, "%02x", digest[k]);
        }

        if(!five && std::strncmp("00000", j, 5) == 0) {
	    std::cout << "00000, i==" << i << ", md5==";
            for (int k = 0; k < 16; k++)
                printf("%02x", digest[k]);

	    std::cout << std::endl;
	    five = true;
        }

        if(!six && std::strncmp("000000", j, 6) == 0) {
	    std::cout << "000000, i==" << i << ", md5==";
            for (int k = 0; k < 16; k++)
                printf("%02x", digest[k]);

	    std::cout << std::endl;
	    six = true;
        }

	if(five && six)
		return;
        i++;
    }
}

#include <thread>
#include <vector>
int main() {
    Md5();
    return 0;
}

// void compute_md5(char *str, unsigned char digest[16]) {
//     MD5_CTX ctx;
//     MD5_Init(&ctx);
//     MD5_Update(&ctx, str, strlen(str));
//     MD5_Final(digest, &ctx);
// }

// int main()
// {
//     unsigned char digest[16];
//     compute_md5("hello world", digest);
//     for (int i = 0; i < 16; i++)
//         printf("%02x", digest[i]);
//     putchar ('\n');
//     return 0;
// }


