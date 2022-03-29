uint32_t get_results(uint32_t channel) {
    static uint32_t calls = 0;
    calls++;
    if (calls > 25) return static_cast<uint32_t>(-1);

    static uint32_t min = 5634, max = 275986;
    static uint32_t min_channel = 3, max_channel = 231;
    static uint32_t zero = 124000;

    if (channel <= min_channel)
        return static_cast<uint32_t>(zero - channel*(static_cast<double>(zero) - min)/min_channel);
    if (channel <= max_channel)
        return static_cast<uint32_t>(min + (static_cast<double>(channel) - min_channel)*(static_cast<double>(max) - min)/(static_cast<double>(max_channel) - min_channel));
    if (channel <= 360)
        return static_cast<uint32_t>(max - (static_cast<double>(channel) - max_channel)*(static_cast<double>(max) - zero)/(static_cast<double>(360) - max_channel));
    return static_cast<uint32_t>(-1);
}
