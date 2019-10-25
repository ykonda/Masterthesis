for (unsigned int channel = 0; channel < numChannels; channel++)
{
  for (unsigned int i = channel; i < framesPerBuffer * numChannels; i += numChannels)
  {
    inBuffer_[channel].buffer.push_back(buf[i]);
  }
}