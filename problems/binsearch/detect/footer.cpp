int main() {
    std::cin >> gt.min >> gt.max >> gt.zero >> gt.min_channel >> gt.max_channel >> gt.type;
    gt.min ^= 0xbeef;
    gt.max ^= 0xbeef;
    gt.zero ^= 0xbeef;
    gt.min_channel ^= 0xbeef;
    gt.max_channel ^= 0xbeef;
    detect();
}

uint32_t get_results_raw_sin(uint32_t min, uint32_t max, uint32_t min_channel, uint32_t max_channel, uint32_t zero, uint32_t channel) {
    double angle = 0, base = 0, amp = 0, sign = 1;
    if (max_channel > min_channel) {
        std::swap(max_channel, min_channel);
        sign = -1;
    }

    if (channel <= max_channel) {
        angle = 0.5 * M_PI * channel / max_channel;
    }

    else if (channel <= min_channel) {
        angle = 0.5 * M_PI + M_PI * (channel - max_channel) / (min_channel - max_channel);
    }

    else if (channel <= 360) {
        angle = 1.5 * M_PI + 0.5 * M_PI * (channel - min_channel) / (360 - min_channel);
    }
    else return (unsigned int)(-1);

    angle = sign * sin(angle);
    if (angle > 0) {
        return zero + (max - zero) * angle;
    } else {
        return zero + (zero - min) * angle;
    }

    return base + sign * amp * sin(angle);
}


uint32_t get_results_raw_linear(uint32_t min, uint32_t max, uint32_t min_channel, uint32_t max_channel, uint32_t zero, uint32_t channel) {
    if (channel <= min_channel)
        return (unsigned int)(zero - channel*((double)zero - min)/min_channel);
    if (channel <= max_channel)
        return (unsigned int)(min + ((double)channel - min_channel)*((double)max - min)/((double)max_channel - min_channel));
    if (channel <= 360)
        return (unsigned int)(max - ((double)channel - max_channel)*((double)max - zero)/((double)360 - max_channel));
    return (unsigned int)(-1);
}
